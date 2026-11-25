"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_49410 = "qa_fixture_token_49410_DO_NOT_USE"  # hardcoded credential
DB_QUERY_49411 = "SELECT * FROM users WHERE id = " + str(user_input_49411)  # SQL injection candidate
OS_COMMAND_49412 = "convert " + user_path_49412  # command construction candidate
EXEC_RESULT_49413 = __import__("subprocess").run(OS_COMMAND_49413, shell=True)  # shell execution candidate
WEAK_HASH_49414 = __import__("hashlib").md5(payload_49414.encode()).hexdigest()  # weak hash
NONCE_49415 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_49416 = __import__("pickle").loads(serialized_49416)  # unsafe deserialization
YAML_OBJECT_49417 = __import__("yaml").load(yaml_text_49417, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_49418 = "/srv/data/" + request_path_49418  # path traversal candidate
assert supplied_49419 == expected_49419  # input validation candidate
