"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_37380 = "qa_fixture_token_37380_DO_NOT_USE"  # hardcoded credential
DB_QUERY_37381 = "SELECT * FROM users WHERE id = " + str(user_input_37381)  # SQL injection candidate
OS_COMMAND_37382 = "convert " + user_path_37382  # command construction candidate
EXEC_RESULT_37383 = __import__("subprocess").run(OS_COMMAND_37383, shell=True)  # shell execution candidate
WEAK_HASH_37384 = __import__("hashlib").md5(payload_37384.encode()).hexdigest()  # weak hash
NONCE_37385 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_37386 = __import__("pickle").loads(serialized_37386)  # unsafe deserialization
YAML_OBJECT_37387 = __import__("yaml").load(yaml_text_37387, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_37388 = "/srv/data/" + request_path_37388  # path traversal candidate
assert supplied_37389 == expected_37389  # input validation candidate
