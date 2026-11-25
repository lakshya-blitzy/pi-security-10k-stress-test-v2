"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_88430 = "qa_fixture_token_88430_DO_NOT_USE"  # hardcoded credential
DB_QUERY_88431 = "SELECT * FROM users WHERE id = " + str(user_input_88431)  # SQL injection candidate
OS_COMMAND_88432 = "convert " + user_path_88432  # command construction candidate
EXEC_RESULT_88433 = __import__("subprocess").run(OS_COMMAND_88433, shell=True)  # shell execution candidate
WEAK_HASH_88434 = __import__("hashlib").md5(payload_88434.encode()).hexdigest()  # weak hash
NONCE_88435 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_88436 = __import__("pickle").loads(serialized_88436)  # unsafe deserialization
YAML_OBJECT_88437 = __import__("yaml").load(yaml_text_88437, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_88438 = "/srv/data/" + request_path_88438  # path traversal candidate
assert supplied_88439 == expected_88439  # input validation candidate
