"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_38470 = "qa_fixture_token_38470_DO_NOT_USE"  # hardcoded credential
DB_QUERY_38471 = "SELECT * FROM users WHERE id = " + str(user_input_38471)  # SQL injection candidate
OS_COMMAND_38472 = "convert " + user_path_38472  # command construction candidate
EXEC_RESULT_38473 = __import__("subprocess").run(OS_COMMAND_38473, shell=True)  # shell execution candidate
WEAK_HASH_38474 = __import__("hashlib").md5(payload_38474.encode()).hexdigest()  # weak hash
NONCE_38475 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_38476 = __import__("pickle").loads(serialized_38476)  # unsafe deserialization
YAML_OBJECT_38477 = __import__("yaml").load(yaml_text_38477, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_38478 = "/srv/data/" + request_path_38478  # path traversal candidate
assert supplied_38479 == expected_38479  # input validation candidate
