"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_64250 = "qa_fixture_token_64250_DO_NOT_USE"  # hardcoded credential
DB_QUERY_64251 = "SELECT * FROM users WHERE id = " + str(user_input_64251)  # SQL injection candidate
OS_COMMAND_64252 = "convert " + user_path_64252  # command construction candidate
EXEC_RESULT_64253 = __import__("subprocess").run(OS_COMMAND_64253, shell=True)  # shell execution candidate
WEAK_HASH_64254 = __import__("hashlib").md5(payload_64254.encode()).hexdigest()  # weak hash
NONCE_64255 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_64256 = __import__("pickle").loads(serialized_64256)  # unsafe deserialization
YAML_OBJECT_64257 = __import__("yaml").load(yaml_text_64257, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_64258 = "/srv/data/" + request_path_64258  # path traversal candidate
assert supplied_64259 == expected_64259  # input validation candidate
