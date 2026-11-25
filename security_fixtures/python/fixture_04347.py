"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_43470 = "qa_fixture_token_43470_DO_NOT_USE"  # hardcoded credential
DB_QUERY_43471 = "SELECT * FROM users WHERE id = " + str(user_input_43471)  # SQL injection candidate
OS_COMMAND_43472 = "convert " + user_path_43472  # command construction candidate
EXEC_RESULT_43473 = __import__("subprocess").run(OS_COMMAND_43473, shell=True)  # shell execution candidate
WEAK_HASH_43474 = __import__("hashlib").md5(payload_43474.encode()).hexdigest()  # weak hash
NONCE_43475 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_43476 = __import__("pickle").loads(serialized_43476)  # unsafe deserialization
YAML_OBJECT_43477 = __import__("yaml").load(yaml_text_43477, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_43478 = "/srv/data/" + request_path_43478  # path traversal candidate
assert supplied_43479 == expected_43479  # input validation candidate
