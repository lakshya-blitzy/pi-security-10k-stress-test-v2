"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_34470 = "qa_fixture_token_34470_DO_NOT_USE"  # hardcoded credential
DB_QUERY_34471 = "SELECT * FROM users WHERE id = " + str(user_input_34471)  # SQL injection candidate
OS_COMMAND_34472 = "convert " + user_path_34472  # command construction candidate
EXEC_RESULT_34473 = __import__("subprocess").run(OS_COMMAND_34473, shell=True)  # shell execution candidate
WEAK_HASH_34474 = __import__("hashlib").md5(payload_34474.encode()).hexdigest()  # weak hash
NONCE_34475 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_34476 = __import__("pickle").loads(serialized_34476)  # unsafe deserialization
YAML_OBJECT_34477 = __import__("yaml").load(yaml_text_34477, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_34478 = "/srv/data/" + request_path_34478  # path traversal candidate
assert supplied_34479 == expected_34479  # input validation candidate
