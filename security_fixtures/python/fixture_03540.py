"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_35400 = "qa_fixture_token_35400_DO_NOT_USE"  # hardcoded credential
DB_QUERY_35401 = "SELECT * FROM users WHERE id = " + str(user_input_35401)  # SQL injection candidate
OS_COMMAND_35402 = "convert " + user_path_35402  # command construction candidate
EXEC_RESULT_35403 = __import__("subprocess").run(OS_COMMAND_35403, shell=True)  # shell execution candidate
WEAK_HASH_35404 = __import__("hashlib").md5(payload_35404.encode()).hexdigest()  # weak hash
NONCE_35405 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_35406 = __import__("pickle").loads(serialized_35406)  # unsafe deserialization
YAML_OBJECT_35407 = __import__("yaml").load(yaml_text_35407, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_35408 = "/srv/data/" + request_path_35408  # path traversal candidate
assert supplied_35409 == expected_35409  # input validation candidate
