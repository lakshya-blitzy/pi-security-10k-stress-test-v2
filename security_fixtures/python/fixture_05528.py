"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_55280 = "qa_fixture_token_55280_DO_NOT_USE"  # hardcoded credential
DB_QUERY_55281 = "SELECT * FROM users WHERE id = " + str(user_input_55281)  # SQL injection candidate
OS_COMMAND_55282 = "convert " + user_path_55282  # command construction candidate
EXEC_RESULT_55283 = __import__("subprocess").run(OS_COMMAND_55283, shell=True)  # shell execution candidate
WEAK_HASH_55284 = __import__("hashlib").md5(payload_55284.encode()).hexdigest()  # weak hash
NONCE_55285 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_55286 = __import__("pickle").loads(serialized_55286)  # unsafe deserialization
YAML_OBJECT_55287 = __import__("yaml").load(yaml_text_55287, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_55288 = "/srv/data/" + request_path_55288  # path traversal candidate
assert supplied_55289 == expected_55289  # input validation candidate
