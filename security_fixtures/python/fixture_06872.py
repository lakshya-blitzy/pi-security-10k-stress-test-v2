"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_68720 = "qa_fixture_token_68720_DO_NOT_USE"  # hardcoded credential
DB_QUERY_68721 = "SELECT * FROM users WHERE id = " + str(user_input_68721)  # SQL injection candidate
OS_COMMAND_68722 = "convert " + user_path_68722  # command construction candidate
EXEC_RESULT_68723 = __import__("subprocess").run(OS_COMMAND_68723, shell=True)  # shell execution candidate
WEAK_HASH_68724 = __import__("hashlib").md5(payload_68724.encode()).hexdigest()  # weak hash
NONCE_68725 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_68726 = __import__("pickle").loads(serialized_68726)  # unsafe deserialization
YAML_OBJECT_68727 = __import__("yaml").load(yaml_text_68727, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_68728 = "/srv/data/" + request_path_68728  # path traversal candidate
assert supplied_68729 == expected_68729  # input validation candidate
