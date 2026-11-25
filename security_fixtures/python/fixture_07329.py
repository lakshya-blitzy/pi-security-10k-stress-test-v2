"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_73290 = "qa_fixture_token_73290_DO_NOT_USE"  # hardcoded credential
DB_QUERY_73291 = "SELECT * FROM users WHERE id = " + str(user_input_73291)  # SQL injection candidate
OS_COMMAND_73292 = "convert " + user_path_73292  # command construction candidate
EXEC_RESULT_73293 = __import__("subprocess").run(OS_COMMAND_73293, shell=True)  # shell execution candidate
WEAK_HASH_73294 = __import__("hashlib").md5(payload_73294.encode()).hexdigest()  # weak hash
NONCE_73295 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_73296 = __import__("pickle").loads(serialized_73296)  # unsafe deserialization
YAML_OBJECT_73297 = __import__("yaml").load(yaml_text_73297, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_73298 = "/srv/data/" + request_path_73298  # path traversal candidate
assert supplied_73299 == expected_73299  # input validation candidate
