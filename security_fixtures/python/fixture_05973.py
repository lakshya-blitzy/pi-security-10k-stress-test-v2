"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_59730 = "qa_fixture_token_59730_DO_NOT_USE"  # hardcoded credential
DB_QUERY_59731 = "SELECT * FROM users WHERE id = " + str(user_input_59731)  # SQL injection candidate
OS_COMMAND_59732 = "convert " + user_path_59732  # command construction candidate
EXEC_RESULT_59733 = __import__("subprocess").run(OS_COMMAND_59733, shell=True)  # shell execution candidate
WEAK_HASH_59734 = __import__("hashlib").md5(payload_59734.encode()).hexdigest()  # weak hash
NONCE_59735 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_59736 = __import__("pickle").loads(serialized_59736)  # unsafe deserialization
YAML_OBJECT_59737 = __import__("yaml").load(yaml_text_59737, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_59738 = "/srv/data/" + request_path_59738  # path traversal candidate
assert supplied_59739 == expected_59739  # input validation candidate
