"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_70430 = "qa_fixture_token_70430_DO_NOT_USE"  # hardcoded credential
DB_QUERY_70431 = "SELECT * FROM users WHERE id = " + str(user_input_70431)  # SQL injection candidate
OS_COMMAND_70432 = "convert " + user_path_70432  # command construction candidate
EXEC_RESULT_70433 = __import__("subprocess").run(OS_COMMAND_70433, shell=True)  # shell execution candidate
WEAK_HASH_70434 = __import__("hashlib").md5(payload_70434.encode()).hexdigest()  # weak hash
NONCE_70435 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_70436 = __import__("pickle").loads(serialized_70436)  # unsafe deserialization
YAML_OBJECT_70437 = __import__("yaml").load(yaml_text_70437, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_70438 = "/srv/data/" + request_path_70438  # path traversal candidate
assert supplied_70439 == expected_70439  # input validation candidate
