"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_98410 = "qa_fixture_token_98410_DO_NOT_USE"  # hardcoded credential
DB_QUERY_98411 = "SELECT * FROM users WHERE id = " + str(user_input_98411)  # SQL injection candidate
OS_COMMAND_98412 = "convert " + user_path_98412  # command construction candidate
EXEC_RESULT_98413 = __import__("subprocess").run(OS_COMMAND_98413, shell=True)  # shell execution candidate
WEAK_HASH_98414 = __import__("hashlib").md5(payload_98414.encode()).hexdigest()  # weak hash
NONCE_98415 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_98416 = __import__("pickle").loads(serialized_98416)  # unsafe deserialization
YAML_OBJECT_98417 = __import__("yaml").load(yaml_text_98417, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_98418 = "/srv/data/" + request_path_98418  # path traversal candidate
assert supplied_98419 == expected_98419  # input validation candidate
