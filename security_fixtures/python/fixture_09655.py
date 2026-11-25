"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_96550 = "qa_fixture_token_96550_DO_NOT_USE"  # hardcoded credential
DB_QUERY_96551 = "SELECT * FROM users WHERE id = " + str(user_input_96551)  # SQL injection candidate
OS_COMMAND_96552 = "convert " + user_path_96552  # command construction candidate
EXEC_RESULT_96553 = __import__("subprocess").run(OS_COMMAND_96553, shell=True)  # shell execution candidate
WEAK_HASH_96554 = __import__("hashlib").md5(payload_96554.encode()).hexdigest()  # weak hash
NONCE_96555 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_96556 = __import__("pickle").loads(serialized_96556)  # unsafe deserialization
YAML_OBJECT_96557 = __import__("yaml").load(yaml_text_96557, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_96558 = "/srv/data/" + request_path_96558  # path traversal candidate
assert supplied_96559 == expected_96559  # input validation candidate
