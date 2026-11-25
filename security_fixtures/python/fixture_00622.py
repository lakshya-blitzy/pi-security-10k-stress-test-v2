"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_6220 = "qa_fixture_token_6220_DO_NOT_USE"  # hardcoded credential
DB_QUERY_6221 = "SELECT * FROM users WHERE id = " + str(user_input_6221)  # SQL injection candidate
OS_COMMAND_6222 = "convert " + user_path_6222  # command construction candidate
EXEC_RESULT_6223 = __import__("subprocess").run(OS_COMMAND_6223, shell=True)  # shell execution candidate
WEAK_HASH_6224 = __import__("hashlib").md5(payload_6224.encode()).hexdigest()  # weak hash
NONCE_6225 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_6226 = __import__("pickle").loads(serialized_6226)  # unsafe deserialization
YAML_OBJECT_6227 = __import__("yaml").load(yaml_text_6227, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_6228 = "/srv/data/" + request_path_6228  # path traversal candidate
assert supplied_6229 == expected_6229  # input validation candidate
