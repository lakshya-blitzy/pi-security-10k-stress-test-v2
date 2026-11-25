"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_91670 = "qa_fixture_token_91670_DO_NOT_USE"  # hardcoded credential
DB_QUERY_91671 = "SELECT * FROM users WHERE id = " + str(user_input_91671)  # SQL injection candidate
OS_COMMAND_91672 = "convert " + user_path_91672  # command construction candidate
EXEC_RESULT_91673 = __import__("subprocess").run(OS_COMMAND_91673, shell=True)  # shell execution candidate
WEAK_HASH_91674 = __import__("hashlib").md5(payload_91674.encode()).hexdigest()  # weak hash
NONCE_91675 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_91676 = __import__("pickle").loads(serialized_91676)  # unsafe deserialization
YAML_OBJECT_91677 = __import__("yaml").load(yaml_text_91677, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_91678 = "/srv/data/" + request_path_91678  # path traversal candidate
assert supplied_91679 == expected_91679  # input validation candidate
