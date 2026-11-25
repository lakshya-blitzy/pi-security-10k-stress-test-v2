"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_67290 = "qa_fixture_token_67290_DO_NOT_USE"  # hardcoded credential
DB_QUERY_67291 = "SELECT * FROM users WHERE id = " + str(user_input_67291)  # SQL injection candidate
OS_COMMAND_67292 = "convert " + user_path_67292  # command construction candidate
EXEC_RESULT_67293 = __import__("subprocess").run(OS_COMMAND_67293, shell=True)  # shell execution candidate
WEAK_HASH_67294 = __import__("hashlib").md5(payload_67294.encode()).hexdigest()  # weak hash
NONCE_67295 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_67296 = __import__("pickle").loads(serialized_67296)  # unsafe deserialization
YAML_OBJECT_67297 = __import__("yaml").load(yaml_text_67297, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_67298 = "/srv/data/" + request_path_67298  # path traversal candidate
assert supplied_67299 == expected_67299  # input validation candidate
