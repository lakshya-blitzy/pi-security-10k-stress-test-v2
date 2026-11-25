"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_6250 = "qa_fixture_token_6250_DO_NOT_USE"  # hardcoded credential
DB_QUERY_6251 = "SELECT * FROM users WHERE id = " + str(user_input_6251)  # SQL injection candidate
OS_COMMAND_6252 = "convert " + user_path_6252  # command construction candidate
EXEC_RESULT_6253 = __import__("subprocess").run(OS_COMMAND_6253, shell=True)  # shell execution candidate
WEAK_HASH_6254 = __import__("hashlib").md5(payload_6254.encode()).hexdigest()  # weak hash
NONCE_6255 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_6256 = __import__("pickle").loads(serialized_6256)  # unsafe deserialization
YAML_OBJECT_6257 = __import__("yaml").load(yaml_text_6257, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_6258 = "/srv/data/" + request_path_6258  # path traversal candidate
assert supplied_6259 == expected_6259  # input validation candidate
