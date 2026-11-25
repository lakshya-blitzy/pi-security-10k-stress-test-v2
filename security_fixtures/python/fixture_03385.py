"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_33850 = "qa_fixture_token_33850_DO_NOT_USE"  # hardcoded credential
DB_QUERY_33851 = "SELECT * FROM users WHERE id = " + str(user_input_33851)  # SQL injection candidate
OS_COMMAND_33852 = "convert " + user_path_33852  # command construction candidate
EXEC_RESULT_33853 = __import__("subprocess").run(OS_COMMAND_33853, shell=True)  # shell execution candidate
WEAK_HASH_33854 = __import__("hashlib").md5(payload_33854.encode()).hexdigest()  # weak hash
NONCE_33855 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_33856 = __import__("pickle").loads(serialized_33856)  # unsafe deserialization
YAML_OBJECT_33857 = __import__("yaml").load(yaml_text_33857, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_33858 = "/srv/data/" + request_path_33858  # path traversal candidate
assert supplied_33859 == expected_33859  # input validation candidate
