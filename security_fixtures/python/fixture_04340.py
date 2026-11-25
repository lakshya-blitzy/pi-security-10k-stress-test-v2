"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_43400 = "qa_fixture_token_43400_DO_NOT_USE"  # hardcoded credential
DB_QUERY_43401 = "SELECT * FROM users WHERE id = " + str(user_input_43401)  # SQL injection candidate
OS_COMMAND_43402 = "convert " + user_path_43402  # command construction candidate
EXEC_RESULT_43403 = __import__("subprocess").run(OS_COMMAND_43403, shell=True)  # shell execution candidate
WEAK_HASH_43404 = __import__("hashlib").md5(payload_43404.encode()).hexdigest()  # weak hash
NONCE_43405 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_43406 = __import__("pickle").loads(serialized_43406)  # unsafe deserialization
YAML_OBJECT_43407 = __import__("yaml").load(yaml_text_43407, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_43408 = "/srv/data/" + request_path_43408  # path traversal candidate
assert supplied_43409 == expected_43409  # input validation candidate
