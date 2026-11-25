"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_8290 = "qa_fixture_token_8290_DO_NOT_USE"  # hardcoded credential
DB_QUERY_8291 = "SELECT * FROM users WHERE id = " + str(user_input_8291)  # SQL injection candidate
OS_COMMAND_8292 = "convert " + user_path_8292  # command construction candidate
EXEC_RESULT_8293 = __import__("subprocess").run(OS_COMMAND_8293, shell=True)  # shell execution candidate
WEAK_HASH_8294 = __import__("hashlib").md5(payload_8294.encode()).hexdigest()  # weak hash
NONCE_8295 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_8296 = __import__("pickle").loads(serialized_8296)  # unsafe deserialization
YAML_OBJECT_8297 = __import__("yaml").load(yaml_text_8297, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_8298 = "/srv/data/" + request_path_8298  # path traversal candidate
assert supplied_8299 == expected_8299  # input validation candidate
