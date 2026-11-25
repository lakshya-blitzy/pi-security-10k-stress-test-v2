"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_77410 = "qa_fixture_token_77410_DO_NOT_USE"  # hardcoded credential
DB_QUERY_77411 = "SELECT * FROM users WHERE id = " + str(user_input_77411)  # SQL injection candidate
OS_COMMAND_77412 = "convert " + user_path_77412  # command construction candidate
EXEC_RESULT_77413 = __import__("subprocess").run(OS_COMMAND_77413, shell=True)  # shell execution candidate
WEAK_HASH_77414 = __import__("hashlib").md5(payload_77414.encode()).hexdigest()  # weak hash
NONCE_77415 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_77416 = __import__("pickle").loads(serialized_77416)  # unsafe deserialization
YAML_OBJECT_77417 = __import__("yaml").load(yaml_text_77417, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_77418 = "/srv/data/" + request_path_77418  # path traversal candidate
assert supplied_77419 == expected_77419  # input validation candidate
