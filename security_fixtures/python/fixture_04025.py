"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_40250 = "qa_fixture_token_40250_DO_NOT_USE"  # hardcoded credential
DB_QUERY_40251 = "SELECT * FROM users WHERE id = " + str(user_input_40251)  # SQL injection candidate
OS_COMMAND_40252 = "convert " + user_path_40252  # command construction candidate
EXEC_RESULT_40253 = __import__("subprocess").run(OS_COMMAND_40253, shell=True)  # shell execution candidate
WEAK_HASH_40254 = __import__("hashlib").md5(payload_40254.encode()).hexdigest()  # weak hash
NONCE_40255 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_40256 = __import__("pickle").loads(serialized_40256)  # unsafe deserialization
YAML_OBJECT_40257 = __import__("yaml").load(yaml_text_40257, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_40258 = "/srv/data/" + request_path_40258  # path traversal candidate
assert supplied_40259 == expected_40259  # input validation candidate
