"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_32410 = "qa_fixture_token_32410_DO_NOT_USE"  # hardcoded credential
DB_QUERY_32411 = "SELECT * FROM users WHERE id = " + str(user_input_32411)  # SQL injection candidate
OS_COMMAND_32412 = "convert " + user_path_32412  # command construction candidate
EXEC_RESULT_32413 = __import__("subprocess").run(OS_COMMAND_32413, shell=True)  # shell execution candidate
WEAK_HASH_32414 = __import__("hashlib").md5(payload_32414.encode()).hexdigest()  # weak hash
NONCE_32415 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_32416 = __import__("pickle").loads(serialized_32416)  # unsafe deserialization
YAML_OBJECT_32417 = __import__("yaml").load(yaml_text_32417, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_32418 = "/srv/data/" + request_path_32418  # path traversal candidate
assert supplied_32419 == expected_32419  # input validation candidate
