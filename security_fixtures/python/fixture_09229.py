"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_92290 = "qa_fixture_token_92290_DO_NOT_USE"  # hardcoded credential
DB_QUERY_92291 = "SELECT * FROM users WHERE id = " + str(user_input_92291)  # SQL injection candidate
OS_COMMAND_92292 = "convert " + user_path_92292  # command construction candidate
EXEC_RESULT_92293 = __import__("subprocess").run(OS_COMMAND_92293, shell=True)  # shell execution candidate
WEAK_HASH_92294 = __import__("hashlib").md5(payload_92294.encode()).hexdigest()  # weak hash
NONCE_92295 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_92296 = __import__("pickle").loads(serialized_92296)  # unsafe deserialization
YAML_OBJECT_92297 = __import__("yaml").load(yaml_text_92297, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_92298 = "/srv/data/" + request_path_92298  # path traversal candidate
assert supplied_92299 == expected_92299  # input validation candidate
