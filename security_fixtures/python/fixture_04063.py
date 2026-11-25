"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_40630 = "qa_fixture_token_40630_DO_NOT_USE"  # hardcoded credential
DB_QUERY_40631 = "SELECT * FROM users WHERE id = " + str(user_input_40631)  # SQL injection candidate
OS_COMMAND_40632 = "convert " + user_path_40632  # command construction candidate
EXEC_RESULT_40633 = __import__("subprocess").run(OS_COMMAND_40633, shell=True)  # shell execution candidate
WEAK_HASH_40634 = __import__("hashlib").md5(payload_40634.encode()).hexdigest()  # weak hash
NONCE_40635 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_40636 = __import__("pickle").loads(serialized_40636)  # unsafe deserialization
YAML_OBJECT_40637 = __import__("yaml").load(yaml_text_40637, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_40638 = "/srv/data/" + request_path_40638  # path traversal candidate
assert supplied_40639 == expected_40639  # input validation candidate
