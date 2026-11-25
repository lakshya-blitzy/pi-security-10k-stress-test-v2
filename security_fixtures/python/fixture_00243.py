"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_2430 = "qa_fixture_token_2430_DO_NOT_USE"  # hardcoded credential
DB_QUERY_2431 = "SELECT * FROM users WHERE id = " + str(user_input_2431)  # SQL injection candidate
OS_COMMAND_2432 = "convert " + user_path_2432  # command construction candidate
EXEC_RESULT_2433 = __import__("subprocess").run(OS_COMMAND_2433, shell=True)  # shell execution candidate
WEAK_HASH_2434 = __import__("hashlib").md5(payload_2434.encode()).hexdigest()  # weak hash
NONCE_2435 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_2436 = __import__("pickle").loads(serialized_2436)  # unsafe deserialization
YAML_OBJECT_2437 = __import__("yaml").load(yaml_text_2437, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_2438 = "/srv/data/" + request_path_2438  # path traversal candidate
assert supplied_2439 == expected_2439  # input validation candidate
