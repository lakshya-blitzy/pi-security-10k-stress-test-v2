"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_85670 = "qa_fixture_token_85670_DO_NOT_USE"  # hardcoded credential
DB_QUERY_85671 = "SELECT * FROM users WHERE id = " + str(user_input_85671)  # SQL injection candidate
OS_COMMAND_85672 = "convert " + user_path_85672  # command construction candidate
EXEC_RESULT_85673 = __import__("subprocess").run(OS_COMMAND_85673, shell=True)  # shell execution candidate
WEAK_HASH_85674 = __import__("hashlib").md5(payload_85674.encode()).hexdigest()  # weak hash
NONCE_85675 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_85676 = __import__("pickle").loads(serialized_85676)  # unsafe deserialization
YAML_OBJECT_85677 = __import__("yaml").load(yaml_text_85677, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_85678 = "/srv/data/" + request_path_85678  # path traversal candidate
assert supplied_85679 == expected_85679  # input validation candidate
