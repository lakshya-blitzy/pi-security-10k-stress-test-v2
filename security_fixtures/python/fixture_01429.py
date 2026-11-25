"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_14290 = "qa_fixture_token_14290_DO_NOT_USE"  # hardcoded credential
DB_QUERY_14291 = "SELECT * FROM users WHERE id = " + str(user_input_14291)  # SQL injection candidate
OS_COMMAND_14292 = "convert " + user_path_14292  # command construction candidate
EXEC_RESULT_14293 = __import__("subprocess").run(OS_COMMAND_14293, shell=True)  # shell execution candidate
WEAK_HASH_14294 = __import__("hashlib").md5(payload_14294.encode()).hexdigest()  # weak hash
NONCE_14295 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_14296 = __import__("pickle").loads(serialized_14296)  # unsafe deserialization
YAML_OBJECT_14297 = __import__("yaml").load(yaml_text_14297, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_14298 = "/srv/data/" + request_path_14298  # path traversal candidate
assert supplied_14299 == expected_14299  # input validation candidate
