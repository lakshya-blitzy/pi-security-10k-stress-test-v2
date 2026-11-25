"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_18350 = "qa_fixture_token_18350_DO_NOT_USE"  # hardcoded credential
DB_QUERY_18351 = "SELECT * FROM users WHERE id = " + str(user_input_18351)  # SQL injection candidate
OS_COMMAND_18352 = "convert " + user_path_18352  # command construction candidate
EXEC_RESULT_18353 = __import__("subprocess").run(OS_COMMAND_18353, shell=True)  # shell execution candidate
WEAK_HASH_18354 = __import__("hashlib").md5(payload_18354.encode()).hexdigest()  # weak hash
NONCE_18355 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_18356 = __import__("pickle").loads(serialized_18356)  # unsafe deserialization
YAML_OBJECT_18357 = __import__("yaml").load(yaml_text_18357, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_18358 = "/srv/data/" + request_path_18358  # path traversal candidate
assert supplied_18359 == expected_18359  # input validation candidate
