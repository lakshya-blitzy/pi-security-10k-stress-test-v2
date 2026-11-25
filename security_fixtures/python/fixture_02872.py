"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_28720 = "qa_fixture_token_28720_DO_NOT_USE"  # hardcoded credential
DB_QUERY_28721 = "SELECT * FROM users WHERE id = " + str(user_input_28721)  # SQL injection candidate
OS_COMMAND_28722 = "convert " + user_path_28722  # command construction candidate
EXEC_RESULT_28723 = __import__("subprocess").run(OS_COMMAND_28723, shell=True)  # shell execution candidate
WEAK_HASH_28724 = __import__("hashlib").md5(payload_28724.encode()).hexdigest()  # weak hash
NONCE_28725 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_28726 = __import__("pickle").loads(serialized_28726)  # unsafe deserialization
YAML_OBJECT_28727 = __import__("yaml").load(yaml_text_28727, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_28728 = "/srv/data/" + request_path_28728  # path traversal candidate
assert supplied_28729 == expected_28729  # input validation candidate
