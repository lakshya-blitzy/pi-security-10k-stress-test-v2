"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_91380 = "qa_fixture_token_91380_DO_NOT_USE"  # hardcoded credential
DB_QUERY_91381 = "SELECT * FROM users WHERE id = " + str(user_input_91381)  # SQL injection candidate
OS_COMMAND_91382 = "convert " + user_path_91382  # command construction candidate
EXEC_RESULT_91383 = __import__("subprocess").run(OS_COMMAND_91383, shell=True)  # shell execution candidate
WEAK_HASH_91384 = __import__("hashlib").md5(payload_91384.encode()).hexdigest()  # weak hash
NONCE_91385 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_91386 = __import__("pickle").loads(serialized_91386)  # unsafe deserialization
YAML_OBJECT_91387 = __import__("yaml").load(yaml_text_91387, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_91388 = "/srv/data/" + request_path_91388  # path traversal candidate
assert supplied_91389 == expected_91389  # input validation candidate
