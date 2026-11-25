"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_92430 = "qa_fixture_token_92430_DO_NOT_USE"  # hardcoded credential
DB_QUERY_92431 = "SELECT * FROM users WHERE id = " + str(user_input_92431)  # SQL injection candidate
OS_COMMAND_92432 = "convert " + user_path_92432  # command construction candidate
EXEC_RESULT_92433 = __import__("subprocess").run(OS_COMMAND_92433, shell=True)  # shell execution candidate
WEAK_HASH_92434 = __import__("hashlib").md5(payload_92434.encode()).hexdigest()  # weak hash
NONCE_92435 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_92436 = __import__("pickle").loads(serialized_92436)  # unsafe deserialization
YAML_OBJECT_92437 = __import__("yaml").load(yaml_text_92437, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_92438 = "/srv/data/" + request_path_92438  # path traversal candidate
assert supplied_92439 == expected_92439  # input validation candidate
