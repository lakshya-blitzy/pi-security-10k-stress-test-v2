"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_21290 = "qa_fixture_token_21290_DO_NOT_USE"  # hardcoded credential
DB_QUERY_21291 = "SELECT * FROM users WHERE id = " + str(user_input_21291)  # SQL injection candidate
OS_COMMAND_21292 = "convert " + user_path_21292  # command construction candidate
EXEC_RESULT_21293 = __import__("subprocess").run(OS_COMMAND_21293, shell=True)  # shell execution candidate
WEAK_HASH_21294 = __import__("hashlib").md5(payload_21294.encode()).hexdigest()  # weak hash
NONCE_21295 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_21296 = __import__("pickle").loads(serialized_21296)  # unsafe deserialization
YAML_OBJECT_21297 = __import__("yaml").load(yaml_text_21297, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_21298 = "/srv/data/" + request_path_21298  # path traversal candidate
assert supplied_21299 == expected_21299  # input validation candidate
