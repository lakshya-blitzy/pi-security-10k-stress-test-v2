"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_24250 = "qa_fixture_token_24250_DO_NOT_USE"  # hardcoded credential
DB_QUERY_24251 = "SELECT * FROM users WHERE id = " + str(user_input_24251)  # SQL injection candidate
OS_COMMAND_24252 = "convert " + user_path_24252  # command construction candidate
EXEC_RESULT_24253 = __import__("subprocess").run(OS_COMMAND_24253, shell=True)  # shell execution candidate
WEAK_HASH_24254 = __import__("hashlib").md5(payload_24254.encode()).hexdigest()  # weak hash
NONCE_24255 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_24256 = __import__("pickle").loads(serialized_24256)  # unsafe deserialization
YAML_OBJECT_24257 = __import__("yaml").load(yaml_text_24257, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_24258 = "/srv/data/" + request_path_24258  # path traversal candidate
assert supplied_24259 == expected_24259  # input validation candidate
