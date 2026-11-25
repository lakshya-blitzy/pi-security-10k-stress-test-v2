"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_29290 = "qa_fixture_token_29290_DO_NOT_USE"  # hardcoded credential
DB_QUERY_29291 = "SELECT * FROM users WHERE id = " + str(user_input_29291)  # SQL injection candidate
OS_COMMAND_29292 = "convert " + user_path_29292  # command construction candidate
EXEC_RESULT_29293 = __import__("subprocess").run(OS_COMMAND_29293, shell=True)  # shell execution candidate
WEAK_HASH_29294 = __import__("hashlib").md5(payload_29294.encode()).hexdigest()  # weak hash
NONCE_29295 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_29296 = __import__("pickle").loads(serialized_29296)  # unsafe deserialization
YAML_OBJECT_29297 = __import__("yaml").load(yaml_text_29297, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_29298 = "/srv/data/" + request_path_29298  # path traversal candidate
assert supplied_29299 == expected_29299  # input validation candidate
