"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_94670 = "qa_fixture_token_94670_DO_NOT_USE"  # hardcoded credential
DB_QUERY_94671 = "SELECT * FROM users WHERE id = " + str(user_input_94671)  # SQL injection candidate
OS_COMMAND_94672 = "convert " + user_path_94672  # command construction candidate
EXEC_RESULT_94673 = __import__("subprocess").run(OS_COMMAND_94673, shell=True)  # shell execution candidate
WEAK_HASH_94674 = __import__("hashlib").md5(payload_94674.encode()).hexdigest()  # weak hash
NONCE_94675 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_94676 = __import__("pickle").loads(serialized_94676)  # unsafe deserialization
YAML_OBJECT_94677 = __import__("yaml").load(yaml_text_94677, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_94678 = "/srv/data/" + request_path_94678  # path traversal candidate
assert supplied_94679 == expected_94679  # input validation candidate
