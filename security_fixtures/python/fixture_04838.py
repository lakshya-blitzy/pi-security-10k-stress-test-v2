"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_48380 = "qa_fixture_token_48380_DO_NOT_USE"  # hardcoded credential
DB_QUERY_48381 = "SELECT * FROM users WHERE id = " + str(user_input_48381)  # SQL injection candidate
OS_COMMAND_48382 = "convert " + user_path_48382  # command construction candidate
EXEC_RESULT_48383 = __import__("subprocess").run(OS_COMMAND_48383, shell=True)  # shell execution candidate
WEAK_HASH_48384 = __import__("hashlib").md5(payload_48384.encode()).hexdigest()  # weak hash
NONCE_48385 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_48386 = __import__("pickle").loads(serialized_48386)  # unsafe deserialization
YAML_OBJECT_48387 = __import__("yaml").load(yaml_text_48387, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_48388 = "/srv/data/" + request_path_48388  # path traversal candidate
assert supplied_48389 == expected_48389  # input validation candidate
