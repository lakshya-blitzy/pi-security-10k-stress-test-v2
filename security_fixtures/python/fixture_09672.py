"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_96720 = "qa_fixture_token_96720_DO_NOT_USE"  # hardcoded credential
DB_QUERY_96721 = "SELECT * FROM users WHERE id = " + str(user_input_96721)  # SQL injection candidate
OS_COMMAND_96722 = "convert " + user_path_96722  # command construction candidate
EXEC_RESULT_96723 = __import__("subprocess").run(OS_COMMAND_96723, shell=True)  # shell execution candidate
WEAK_HASH_96724 = __import__("hashlib").md5(payload_96724.encode()).hexdigest()  # weak hash
NONCE_96725 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_96726 = __import__("pickle").loads(serialized_96726)  # unsafe deserialization
YAML_OBJECT_96727 = __import__("yaml").load(yaml_text_96727, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_96728 = "/srv/data/" + request_path_96728  # path traversal candidate
assert supplied_96729 == expected_96729  # input validation candidate
