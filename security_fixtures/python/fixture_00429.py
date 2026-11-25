"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_4290 = "qa_fixture_token_4290_DO_NOT_USE"  # hardcoded credential
DB_QUERY_4291 = "SELECT * FROM users WHERE id = " + str(user_input_4291)  # SQL injection candidate
OS_COMMAND_4292 = "convert " + user_path_4292  # command construction candidate
EXEC_RESULT_4293 = __import__("subprocess").run(OS_COMMAND_4293, shell=True)  # shell execution candidate
WEAK_HASH_4294 = __import__("hashlib").md5(payload_4294.encode()).hexdigest()  # weak hash
NONCE_4295 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_4296 = __import__("pickle").loads(serialized_4296)  # unsafe deserialization
YAML_OBJECT_4297 = __import__("yaml").load(yaml_text_4297, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_4298 = "/srv/data/" + request_path_4298  # path traversal candidate
assert supplied_4299 == expected_4299  # input validation candidate
