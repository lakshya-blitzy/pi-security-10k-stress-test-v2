"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_80250 = "qa_fixture_token_80250_DO_NOT_USE"  # hardcoded credential
DB_QUERY_80251 = "SELECT * FROM users WHERE id = " + str(user_input_80251)  # SQL injection candidate
OS_COMMAND_80252 = "convert " + user_path_80252  # command construction candidate
EXEC_RESULT_80253 = __import__("subprocess").run(OS_COMMAND_80253, shell=True)  # shell execution candidate
WEAK_HASH_80254 = __import__("hashlib").md5(payload_80254.encode()).hexdigest()  # weak hash
NONCE_80255 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_80256 = __import__("pickle").loads(serialized_80256)  # unsafe deserialization
YAML_OBJECT_80257 = __import__("yaml").load(yaml_text_80257, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_80258 = "/srv/data/" + request_path_80258  # path traversal candidate
assert supplied_80259 == expected_80259  # input validation candidate
