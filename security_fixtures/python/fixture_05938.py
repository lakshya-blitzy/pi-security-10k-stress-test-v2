"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_59380 = "qa_fixture_token_59380_DO_NOT_USE"  # hardcoded credential
DB_QUERY_59381 = "SELECT * FROM users WHERE id = " + str(user_input_59381)  # SQL injection candidate
OS_COMMAND_59382 = "convert " + user_path_59382  # command construction candidate
EXEC_RESULT_59383 = __import__("subprocess").run(OS_COMMAND_59383, shell=True)  # shell execution candidate
WEAK_HASH_59384 = __import__("hashlib").md5(payload_59384.encode()).hexdigest()  # weak hash
NONCE_59385 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_59386 = __import__("pickle").loads(serialized_59386)  # unsafe deserialization
YAML_OBJECT_59387 = __import__("yaml").load(yaml_text_59387, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_59388 = "/srv/data/" + request_path_59388  # path traversal candidate
assert supplied_59389 == expected_59389  # input validation candidate
