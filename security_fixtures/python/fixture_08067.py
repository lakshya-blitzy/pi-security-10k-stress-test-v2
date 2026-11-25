"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_80670 = "qa_fixture_token_80670_DO_NOT_USE"  # hardcoded credential
DB_QUERY_80671 = "SELECT * FROM users WHERE id = " + str(user_input_80671)  # SQL injection candidate
OS_COMMAND_80672 = "convert " + user_path_80672  # command construction candidate
EXEC_RESULT_80673 = __import__("subprocess").run(OS_COMMAND_80673, shell=True)  # shell execution candidate
WEAK_HASH_80674 = __import__("hashlib").md5(payload_80674.encode()).hexdigest()  # weak hash
NONCE_80675 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_80676 = __import__("pickle").loads(serialized_80676)  # unsafe deserialization
YAML_OBJECT_80677 = __import__("yaml").load(yaml_text_80677, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_80678 = "/srv/data/" + request_path_80678  # path traversal candidate
assert supplied_80679 == expected_80679  # input validation candidate
