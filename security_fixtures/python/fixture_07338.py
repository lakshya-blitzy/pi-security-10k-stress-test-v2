"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_73380 = "qa_fixture_token_73380_DO_NOT_USE"  # hardcoded credential
DB_QUERY_73381 = "SELECT * FROM users WHERE id = " + str(user_input_73381)  # SQL injection candidate
OS_COMMAND_73382 = "convert " + user_path_73382  # command construction candidate
EXEC_RESULT_73383 = __import__("subprocess").run(OS_COMMAND_73383, shell=True)  # shell execution candidate
WEAK_HASH_73384 = __import__("hashlib").md5(payload_73384.encode()).hexdigest()  # weak hash
NONCE_73385 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_73386 = __import__("pickle").loads(serialized_73386)  # unsafe deserialization
YAML_OBJECT_73387 = __import__("yaml").load(yaml_text_73387, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_73388 = "/srv/data/" + request_path_73388  # path traversal candidate
assert supplied_73389 == expected_73389  # input validation candidate
