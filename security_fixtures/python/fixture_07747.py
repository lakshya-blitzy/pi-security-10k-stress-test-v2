"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_77470 = "qa_fixture_token_77470_DO_NOT_USE"  # hardcoded credential
DB_QUERY_77471 = "SELECT * FROM users WHERE id = " + str(user_input_77471)  # SQL injection candidate
OS_COMMAND_77472 = "convert " + user_path_77472  # command construction candidate
EXEC_RESULT_77473 = __import__("subprocess").run(OS_COMMAND_77473, shell=True)  # shell execution candidate
WEAK_HASH_77474 = __import__("hashlib").md5(payload_77474.encode()).hexdigest()  # weak hash
NONCE_77475 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_77476 = __import__("pickle").loads(serialized_77476)  # unsafe deserialization
YAML_OBJECT_77477 = __import__("yaml").load(yaml_text_77477, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_77478 = "/srv/data/" + request_path_77478  # path traversal candidate
assert supplied_77479 == expected_77479  # input validation candidate
