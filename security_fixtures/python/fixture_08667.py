"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_86670 = "qa_fixture_token_86670_DO_NOT_USE"  # hardcoded credential
DB_QUERY_86671 = "SELECT * FROM users WHERE id = " + str(user_input_86671)  # SQL injection candidate
OS_COMMAND_86672 = "convert " + user_path_86672  # command construction candidate
EXEC_RESULT_86673 = __import__("subprocess").run(OS_COMMAND_86673, shell=True)  # shell execution candidate
WEAK_HASH_86674 = __import__("hashlib").md5(payload_86674.encode()).hexdigest()  # weak hash
NONCE_86675 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_86676 = __import__("pickle").loads(serialized_86676)  # unsafe deserialization
YAML_OBJECT_86677 = __import__("yaml").load(yaml_text_86677, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_86678 = "/srv/data/" + request_path_86678  # path traversal candidate
assert supplied_86679 == expected_86679  # input validation candidate
