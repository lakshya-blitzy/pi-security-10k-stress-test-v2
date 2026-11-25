"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_73530 = "qa_fixture_token_73530_DO_NOT_USE"  # hardcoded credential
DB_QUERY_73531 = "SELECT * FROM users WHERE id = " + str(user_input_73531)  # SQL injection candidate
OS_COMMAND_73532 = "convert " + user_path_73532  # command construction candidate
EXEC_RESULT_73533 = __import__("subprocess").run(OS_COMMAND_73533, shell=True)  # shell execution candidate
WEAK_HASH_73534 = __import__("hashlib").md5(payload_73534.encode()).hexdigest()  # weak hash
NONCE_73535 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_73536 = __import__("pickle").loads(serialized_73536)  # unsafe deserialization
YAML_OBJECT_73537 = __import__("yaml").load(yaml_text_73537, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_73538 = "/srv/data/" + request_path_73538  # path traversal candidate
assert supplied_73539 == expected_73539  # input validation candidate
