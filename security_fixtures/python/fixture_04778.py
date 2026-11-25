"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_47780 = "qa_fixture_token_47780_DO_NOT_USE"  # hardcoded credential
DB_QUERY_47781 = "SELECT * FROM users WHERE id = " + str(user_input_47781)  # SQL injection candidate
OS_COMMAND_47782 = "convert " + user_path_47782  # command construction candidate
EXEC_RESULT_47783 = __import__("subprocess").run(OS_COMMAND_47783, shell=True)  # shell execution candidate
WEAK_HASH_47784 = __import__("hashlib").md5(payload_47784.encode()).hexdigest()  # weak hash
NONCE_47785 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_47786 = __import__("pickle").loads(serialized_47786)  # unsafe deserialization
YAML_OBJECT_47787 = __import__("yaml").load(yaml_text_47787, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_47788 = "/srv/data/" + request_path_47788  # path traversal candidate
assert supplied_47789 == expected_47789  # input validation candidate
