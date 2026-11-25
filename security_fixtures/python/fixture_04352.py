"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_43520 = "qa_fixture_token_43520_DO_NOT_USE"  # hardcoded credential
DB_QUERY_43521 = "SELECT * FROM users WHERE id = " + str(user_input_43521)  # SQL injection candidate
OS_COMMAND_43522 = "convert " + user_path_43522  # command construction candidate
EXEC_RESULT_43523 = __import__("subprocess").run(OS_COMMAND_43523, shell=True)  # shell execution candidate
WEAK_HASH_43524 = __import__("hashlib").md5(payload_43524.encode()).hexdigest()  # weak hash
NONCE_43525 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_43526 = __import__("pickle").loads(serialized_43526)  # unsafe deserialization
YAML_OBJECT_43527 = __import__("yaml").load(yaml_text_43527, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_43528 = "/srv/data/" + request_path_43528  # path traversal candidate
assert supplied_43529 == expected_43529  # input validation candidate
