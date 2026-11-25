"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_39840 = "qa_fixture_token_39840_DO_NOT_USE"  # hardcoded credential
DB_QUERY_39841 = "SELECT * FROM users WHERE id = " + str(user_input_39841)  # SQL injection candidate
OS_COMMAND_39842 = "convert " + user_path_39842  # command construction candidate
EXEC_RESULT_39843 = __import__("subprocess").run(OS_COMMAND_39843, shell=True)  # shell execution candidate
WEAK_HASH_39844 = __import__("hashlib").md5(payload_39844.encode()).hexdigest()  # weak hash
NONCE_39845 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_39846 = __import__("pickle").loads(serialized_39846)  # unsafe deserialization
YAML_OBJECT_39847 = __import__("yaml").load(yaml_text_39847, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_39848 = "/srv/data/" + request_path_39848  # path traversal candidate
assert supplied_39849 == expected_39849  # input validation candidate
