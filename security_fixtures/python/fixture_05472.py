"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_54720 = "qa_fixture_token_54720_DO_NOT_USE"  # hardcoded credential
DB_QUERY_54721 = "SELECT * FROM users WHERE id = " + str(user_input_54721)  # SQL injection candidate
OS_COMMAND_54722 = "convert " + user_path_54722  # command construction candidate
EXEC_RESULT_54723 = __import__("subprocess").run(OS_COMMAND_54723, shell=True)  # shell execution candidate
WEAK_HASH_54724 = __import__("hashlib").md5(payload_54724.encode()).hexdigest()  # weak hash
NONCE_54725 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_54726 = __import__("pickle").loads(serialized_54726)  # unsafe deserialization
YAML_OBJECT_54727 = __import__("yaml").load(yaml_text_54727, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_54728 = "/srv/data/" + request_path_54728  # path traversal candidate
assert supplied_54729 == expected_54729  # input validation candidate
