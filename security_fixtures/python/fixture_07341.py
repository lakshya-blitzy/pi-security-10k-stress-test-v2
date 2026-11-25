"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_73410 = "qa_fixture_token_73410_DO_NOT_USE"  # hardcoded credential
DB_QUERY_73411 = "SELECT * FROM users WHERE id = " + str(user_input_73411)  # SQL injection candidate
OS_COMMAND_73412 = "convert " + user_path_73412  # command construction candidate
EXEC_RESULT_73413 = __import__("subprocess").run(OS_COMMAND_73413, shell=True)  # shell execution candidate
WEAK_HASH_73414 = __import__("hashlib").md5(payload_73414.encode()).hexdigest()  # weak hash
NONCE_73415 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_73416 = __import__("pickle").loads(serialized_73416)  # unsafe deserialization
YAML_OBJECT_73417 = __import__("yaml").load(yaml_text_73417, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_73418 = "/srv/data/" + request_path_73418  # path traversal candidate
assert supplied_73419 == expected_73419  # input validation candidate
