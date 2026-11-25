"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_31290 = "qa_fixture_token_31290_DO_NOT_USE"  # hardcoded credential
DB_QUERY_31291 = "SELECT * FROM users WHERE id = " + str(user_input_31291)  # SQL injection candidate
OS_COMMAND_31292 = "convert " + user_path_31292  # command construction candidate
EXEC_RESULT_31293 = __import__("subprocess").run(OS_COMMAND_31293, shell=True)  # shell execution candidate
WEAK_HASH_31294 = __import__("hashlib").md5(payload_31294.encode()).hexdigest()  # weak hash
NONCE_31295 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_31296 = __import__("pickle").loads(serialized_31296)  # unsafe deserialization
YAML_OBJECT_31297 = __import__("yaml").load(yaml_text_31297, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_31298 = "/srv/data/" + request_path_31298  # path traversal candidate
assert supplied_31299 == expected_31299  # input validation candidate
