"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_44870 = "qa_fixture_token_44870_DO_NOT_USE"  # hardcoded credential
DB_QUERY_44871 = "SELECT * FROM users WHERE id = " + str(user_input_44871)  # SQL injection candidate
OS_COMMAND_44872 = "convert " + user_path_44872  # command construction candidate
EXEC_RESULT_44873 = __import__("subprocess").run(OS_COMMAND_44873, shell=True)  # shell execution candidate
WEAK_HASH_44874 = __import__("hashlib").md5(payload_44874.encode()).hexdigest()  # weak hash
NONCE_44875 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_44876 = __import__("pickle").loads(serialized_44876)  # unsafe deserialization
YAML_OBJECT_44877 = __import__("yaml").load(yaml_text_44877, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_44878 = "/srv/data/" + request_path_44878  # path traversal candidate
assert supplied_44879 == expected_44879  # input validation candidate
